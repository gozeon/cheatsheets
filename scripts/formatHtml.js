const _ = require('lodash')

function formatHtml(target) {
  const pureArr = _.filter(target, (item) => item !== '\n')
  const indexWithHeader1 = []
  _.forEach(pureArr, (item, index) => {
    if (item?.tag === 'h1') {
      indexWithHeader1.push(index)
    }
  })

  const result = []

  // 包装h1
  for (let i = 0; i <= indexWithHeader1.length; i++) {
    if (i === 0) {
      // before
      result.push(_.slice(pureArr, 0, indexWithHeader1[i]))
    } else {
      const arrWithHeader3 = _.slice(
        pureArr,
        indexWithHeader1[i - 1],
        indexWithHeader1[i]
      )
      result.push(arrWithHeader3.shift())
      const boxDiv = {
        tag: 'div',
        attrs: { class: 'box' },
        content: arrWithHeader3,
      }
      // 包装h3
      const indexWithHeader3 = []
      const resultWithHeader3 = []
      _.forEach(arrWithHeader3, (item, index) => {
        if (item?.tag === 'h3') {
          indexWithHeader3.push(index)
        }
      })
      for (let j = 0; j <= indexWithHeader3.length; j++) {
        if (j === 0) {
          // before
          resultWithHeader3.push(
            _.slice(arrWithHeader3, 0, indexWithHeader3[j])
          )
        } else {
          const tmp = _.slice(
            arrWithHeader3,
            indexWithHeader3[j - 1],
            indexWithHeader3[j]
          )
          const itemDiv = { tag: 'div', attrs: { class: 'item' }, content: tmp }
          resultWithHeader3.push(itemDiv)
        }
      }
      result.push({
        tag: 'div',
        attrs: { class: 'box' },
        content: _.flatten(resultWithHeader3),
      })
    }
  }

  return _.flatten(result)
}

exports.formatHtml = formatHtml
