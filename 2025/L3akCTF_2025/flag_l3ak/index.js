const express = require('express');
const path = require('path');
const app = express();

const FLAG = 'L3AK{t3mp_flag!!}'
const PORT = 3000;

app.use(express.json());
app.use(express.static('public'));

const posts = [
    {
        id: 1,
        title: "Welcome to our blog!",
        content: "This is our first post. Welcome everyone!",
        author: "admin",
        date: "2025-01-15"
    },
    {
        id: 2,
        title: "Tech Tips",
        content: "Here are some useful technology tips for beginners. Always keep your software updated!",
        author: "Some guy out there",
        date: "2025-01-20"
    },
    {
        id: 3,
        title: "Not the flag?",
        content: `Well luckily the content of the flag is hidden so here it is: ${FLAG}`,
        author: "admin",
        date: "2025-05-13"
    },
    {
        id: 4,
        title: "Real flag fr",
        content: `Forget that other flag. Here is a flag: L3AK{Bad_bl0g?}`,
        author: "L3ak Member",
        date: "2025-06-13"
    },
    {
        id: 5,
        title: "Did you know?",
        content: "This blog post site is pretty dope, right?",
        author: "???",
        date: "2025-06-20"
    },
];

app.get('/', (_, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

app.post('/api/search', (req, res) => {
    const { query } = req.body;
    
    if (!query || typeof query !== 'string' || query.length !== 3) {
        return res.status(400).json({ 
            error: 'Query must be 3 characters.',
        });
    }

    const matchingPosts = posts
        .filter(post => 
            post.title.includes(query) ||
            post.content.includes(query) ||
            post.author.includes(query)
        )
        .map(post => ({
            ...post,
            content: post.content.replace(FLAG, '*'.repeat(FLAG.length))
    }));

    res.json({
        results: matchingPosts,
        count: matchingPosts.length,
        query: query
    });
});

app.get('/api/posts', (_, res) => {
    const publicPosts = posts.map(post => ({
        id: post.id,
        title: post.title,
        content: post.content.replace(FLAG, '*'.repeat(FLAG.length)),
        author: post.author,
        date: post.date
    }));
    
    res.json({
        posts: publicPosts,
        total: publicPosts.length
    });
});

app.use((_, res) => {
    res.status(404).json({ error: 'Endpoint not found' });
});

app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
