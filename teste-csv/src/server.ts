import express from 'express';
import multer from 'multer';
import uploadConfig from '../config/upload';


const app = express();
const upload = multer(uploadConfig);

app.post('/', upload.single('file'), (request, response) => {
  return response.json({ ok: true });
})

app.listen(3333, () => {
  console.log('Server started on port 3333');
});