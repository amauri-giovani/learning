import { Request, Response } from 'express';
import createUser from './services/createUser';


export function users (request: Request, response: Response) {
  const user = createUser({
    name:'Amauri',
    email: 'amauri@gmail.com',
    password: 12345,
    techs: ['JS', 'C#'], 
    experience: {backend: true, frontend: false}
  });
  return response.json({ usuario: user });
}