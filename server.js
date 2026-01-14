const express = require("express");
const app = express();
const PORT = process.env.PORT || 3000;


app.get("/posts", (req, res) => {
  res.send("Getting all posts");
});

app.listen(PORT, () => {
  console.log(`Server is running on port http://localhost:${PORT}`);
});
