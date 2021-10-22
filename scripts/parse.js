const posthtml = require('posthtml')
const postParser = require('posthtml-parser')
const { formatHtml } = require('./formatHtml')

async function genHtml(ast) {
  return new Promise((resolve, reject) => {
    posthtml()
      .use((tree) => {
        return ast
      })
      .process('', {})
      .then((result) => {
        resolve(result.html)
      })
      .catch((err) => reject(err))
  })
}

async function parser(target) {
  return new Promise((resolve, reject) => {
    posthtml()
      .use((tree) => {
        const ast = postParser.parser(target)
        return formatHtml(ast)
      })
      .process('', {})
      .then((result) => {
        resolve(result.html)
      })
      .catch((err) => reject(err))
  })
}

exports.parser = parser
exports.genHtml = genHtml
