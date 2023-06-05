var express = require('express')
const { MongoClient } = require('mongodb')
const uri = "mongodb://mongo:27017"
const client = new MongoClient(uri, { useUnifiedTopology: true })

async function initApi() {
    await client.connect()
    const router = express.Router()
    const secretDataDb = client.db("secretData")
    const postsCollection = secretDataDb.collection('posts')

    router.get('/', (req, res) => {
        res.send("Hello World!")
    })

    router.get('/posts', (req, res) => {
        postsCollection.find(req.query).limit(5).toArray().then(posts => {
            posts.forEach(post => {
                if (post.flag) {
                    post.flag = "[REDACTED] Flag format detected - redacted by WAF"
                }
            })
            res.send(posts)
        })
        .catch(err => {
            res.status(500).send(err.message)
        })
    })
    return router
}
module.exports = initApi
