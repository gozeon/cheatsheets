const fg = require('fast-glob')
const path = require('path')
const fs = require('fs-extra')
const ejs = require('ejs')
const _ = require('lodash')
const { marked } = require('./marked')
const { parser, genHtml } = require('./parse')
const { metaData } = require('./meta')

const mdFolder = path.join(__dirname, '..', 'doc')
const indexTmpFile = path.join(__dirname, '..', 'template/index.html')
const docTmpFile = path.join(__dirname, '..', 'template/doc.html')
const hhtmlFolder = path.join(__dirname, '..', 'docs')

fg('*.md', {
  cwd: mdFolder,
  absolute: true,
}).then(async (files) => {
  // render Doc
  const promises = files.map(async (file) => {
    const { attributes, body } = await metaData(file)
    const pageData = {
      ...attributes,
      intro: marked(attributes?.intro || ''),
      document: await parser(marked(body)),
    }
    const htmlScope = path.parse(file).name

    ejs.renderFile(docTmpFile, pageData, { cache: true }, function (err, str) {
      fs.outputFileSync(
        path.join(hhtmlFolder, htmlScope, 'index.html'),
        str,
        'utf-8'
      )
    })
    return { ...attributes, htmlScope }
  })

  const attributes = await Promise.all(promises)
  const category = _.uniq(
    _.flatten(_.map(attributes, (item) => _.split(item?.category || '', ',')))
  )

  // render index.html
  const result = _.map(category, (item) => {
    const docs = _.filter(attributes, (doc) => _.includes(doc.category, item))

    const aTag = {
      tag: 'a',
      attars: { class: 'item', href: '' },
      content: '',
    }

    return [
      {
        tag: 'h3',
        content: item,
      },
      {
        tag: 'div',
        attrs: {
          class: 'box',
        },
        content: _.map(docs, (doc) => ({
          tag: 'a',
          attrs: { class: 'item', href: doc.htmlScope },
          content: doc.title,
        })),
      },
    ]
  })

  const document = await genHtml(_.flatten(result))

  ejs.renderFile(
    indexTmpFile,
    { document },
    { cache: true },
    function (err, str) {
      fs.outputFileSync(path.join(hhtmlFolder, 'index.html'), str, 'utf-8')
    }
  )
})
