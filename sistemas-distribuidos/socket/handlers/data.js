

module.exports.formatData = buffer => JSON.parse(buffer.toString())
module.exports.encodeData = data => JSON.stringify(data)
