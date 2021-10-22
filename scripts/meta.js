const fs = require('fs-extra')
const fm = require('front-matter')

function metaData(filePath) {
  return new Promise((resolve, reject) => {
    fs.readFile(filePath, 'utf8', function (err, data) {
      if (err) {
        reject(err)
      }

      const metaData = fm(data)

      resolve(metaData)
    })
  })
}

exports.metaData = metaData
