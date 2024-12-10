interface XPuser {
  backend: boolean,
  frontend: boolean
}

interface dataUser {
  name: string,
  email: string,
  password: number,
  techs: string[],
  experience: XPuser
}

export default function createUser({ name, email, password, techs, experience }: dataUser) {
  const user = {
    name,
    email,
    password,
    techs,
    experience
  }
  return user;
}