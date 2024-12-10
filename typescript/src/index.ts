import express from 'express';
import { users } from './routes';

const app = express();

app.get('/', users);

app.listen(3333);