const express = require('express');
const cors = require('cors');
const { uuid, isUuid } = require('uuidv4');

const app = express();

app.use(express.json());
app.use(cors());
app.listen(3333);

const repositories = [];

app.get('/repositories', (request, response) => {
  return response.json(repositories);
}
);

app.post('/repositories', (request, response) => {
  const { url, title, techs } = request.body;
  const repository = {
    id: uuid(),
    url,
    title,
    techs
  }
  repositories.push(repository);
  return response.json(repository);
});

app.put('/repositories/:id', (request, response) => {
  const { id } = request.params;
  const { url, title, techs } = request.body;
  const repoIndex = repositories.findIndex(repo => repo.id === id);
  if (repoIndex < 0) {
    return response.status(404).json({ error: 'Repository not found.' })
  }
  const repository = {
    id,
    url,
    title,
    techs
  }
  repositories[repoIndex] = repository
  return response.json(repository);
});

app.delete('/repositories/:id', (request, response) => {
  const { id } = request.params;
  const { url, title, techs } = request.body;
  const repoIndex = repositories.findIndex(repo => repo.id === id);
  if (repoIndex < 0) {
    return response.status(404).json({ error: 'Repository not found.' })
  }
  repositories.splice(repoIndex, 1);
  return response.status(204).send();
});