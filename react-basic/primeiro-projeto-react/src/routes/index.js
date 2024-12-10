import React from 'react';
import TodosPKMN from '../pages/Todos';
import MeusPKMN from '../pages/Meus';
import {Switch, Route} from 'react-router-dom';


const Routes = () => (
  <Switch>
    <Route exact path="/" component={TodosPKMN} />
    <Route path="/Meus" component={MeusPKMN} />
  </Switch>
)

export default Routes;
