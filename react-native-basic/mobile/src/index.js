import React, { useState, useEffect } from 'react';
import api from './services/api';
import {
  View,
  Text,
  StyleSheet,
  TouchableOpacity,
  FlatList,
  SafeAreaView
} from 'react-native';


// export default function App() {
//   const [repositories, setRepositories] = useState([]);

//   useEffect(() => {
//     api.get('repositories').then(response => {
//       setRepositories(response.data);
//     })
//   }, []);

//   function all_repos() {
//     console.log(repositories);
//   }

//   return (
//     <FlatList
//       data={repositories}
//       keyExtractor={repository => repository.id}
//       renderItem={({ item: repository }) => (
//         <View style={styles.container}>
//           <Text style={styles.project}>Repositório: {repository.title}</Text>
//           <Text style={styles.tech}>Tecnologias:</Text>
//         {repository.techs.map(tech => (
//           <Text key={tech} style={styles.tech}>
//             {tech}
//           </Text>
//         ))}
//         </View>
//       )}
//     />
//   );
// }


export default function App() {
  const lista = [
    { id: "1", name: 'Amauri', linguagens: ['Python', 'C++', 'C#'] },
    { id: "2", name: 'Giovani', linguagens: ['React', 'Node', 'JS'] },
  ]
  return (
    <>
    <SafeAreaView style={styles.container}>
      <FlatList
        data={lista}
        keyExtractor={item => item.id}
        renderItem={({item}) => (
          <View style={styles.container}>
            <Text style={styles.buttonText}>{item.name}</Text>
            {item.linguagens.map(linguagem => (
              <Text key={Math.random().toString()} style={styles.buttonText}>{linguagem}</Text>
            ))}
          </View>
        )}
      />
      </SafeAreaView>
    </>
  );
}



const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#222',
    justifyContent: 'center',
    alignItems: 'center',
  },
  project: {
    color: '#DDD',
    fontWeight: 'bold',
    fontSize: 32,
  },
  tech: {
    color: '#FFF',
    fontSize: 20
  },
  button: {
    backgroundColor: '#000',
    margin: 20,
    height: 50,
    borderRadius: 6,
    justifyContent: 'center',
    alignItems: 'center'
  },
  buttonText: {
    padding: 10,
    color: '#DDD',
  }
})

  // < TouchableOpacity style = { styles.button } >
  //   <Text style={styles.buttonText}>Adicionar repositório</Text>
  //         </TouchableOpacity >