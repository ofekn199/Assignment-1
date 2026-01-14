const express = require("express");
const app = express();
const PORT = process.env.PORT || 3000;
const postRoutes = require("./routes/postRoutes"); 

app.use("/posts", postRoutes);

app.listen(PORT, () => {
  console.log(`Server is running on port http://localhost:${PORT}`);
});
