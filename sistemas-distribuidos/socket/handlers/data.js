

module.exports.formatData = buffer => {
    if (typeof buffer === 'string') {
        return JSON.parse(buffer)
    }
    const str = new TextDecoder().decode(buffer)
    const js = JSON.parse(str)
    return js
}
module.exports.encodeData = data => JSON.stringify(data)
