/**
 * Sample React Native App
 * https://github.com/facebook/react-native
 *
 * @format
 */

import React from 'react';
import {useState} from 'react';
import type {PropsWithChildren} from 'react';
import {
  SafeAreaView,
  StatusBar,
  StyleSheet,
  Text,
  useColorScheme,
  View,
  Alert,
  Pressable,
  TextInput,
  ScrollView,

} from 'react-native';

import {
  Colors,
} from 'react-native/Libraries/NewAppScreen';

type SectionProps = PropsWithChildren<{
  title: string;
}>;



function App(): JSX.Element {
  const isDarkMode = useColorScheme() === 'dark';
  const [text, changeText] = useState('');


  const backgroundStyle = {
    backgroundColor: isDarkMode ? Colors.darker : Colors.lighter,
  };

  return (
    <SafeAreaView style={{...backgroundStyle,height:1000}}>
      <StatusBar
//         barStyle={isDarkMode ? 'light-content' : 'dark-content'}
        barStyle={'light-content'}
        backgroundColor={Colors.darker}
      />
      <View style={styles.viewStyle}>
        <Text
       style={[styles.textStyle,{color: isDarkMode ? 'white': 'black'}]}>
        Hello
       </Text>
       </View>
      <TextInput style={{
        height: 30,
        width: 80,
        padding: 5,
        marginStart: 'auto',
        marginEnd: 'auto',
        marginBottom: 5,
        backgroundColor: isDarkMode ? '#666564': '#e8e7e6',
        borderRadius: 5,
        color: isDarkMode ? 'white': 'black'
      }}
      onChangeText={changeText}
      value={text}
      />

      <Pressable style={[styles.buttonStyle,]}
      onPress={() => Alert.alert('Greetings!',`Hello! ${text}`)}
      >
        {/* {({pressed}) => (
          <Text style={{
            marginStart: 'auto',
            marginEnd: 'auto'
          }}>{(pressed) ? 'Stop pressing me!': 'Press Me !'}</Text>
        )} */}
        <Text style={{
            marginStart: 'auto',
            marginEnd: 'auto',
            
          }} >Press Me!</Text>
      </Pressable>

    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
    textStyle: {
      fontSize: 35
    },
    viewStyle: {
      marginTop: 200,
      marginStart: 'auto',
      marginEnd: 'auto',
      borderStyle: 'solid',
      // backgroundColor: '#b1edfa',
      // color: 'red'
    },
    buttonStyle: {
      width: 100,
      paddingTop: 5,
      paddingBottom: 5,
      marginEnd: 'auto',
      marginStart: 'auto',
      backgroundColor:  '#0476b8',
      // color: isDarkMode ? 'white': 'black',
      color: 'black',
      borderRadius: 5,

    }
});

export default App;
