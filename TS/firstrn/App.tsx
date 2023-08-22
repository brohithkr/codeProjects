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


  // const backgroundStyle = {
  //   backgroundColor: isDarkMode ? Colors.darker : Colors.lighter,
  // };

  return (
    <SafeAreaView >
      <StatusBar
//         barStyle={isDarkMode ? 'light-content' : 'dark-content'}
        barStyle={'light-content'}
        backgroundColor={Colors.darker}
      />
      <View style={styles.viewStyle}><Text style={styles.textStyle}>Hello</Text></View>
      <TextInput style={{
        height: 30,
        width: 80,
        padding: 5,
        marginStart: 'auto',
        marginEnd: 'auto',
        marginBottom: 5,
        backgroundColor: '#e8e7e6',
        borderRadius: 5
      }}
      onChangeText={changeText}
      value={text}
      />

      <Pressable style={[styles.buttonStyle, /*({pressed}) => ((pressed) ?{ backgroundColor: "red" }*/]}
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
            marginEnd: 'auto'
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
      width: 200,
      marginEnd: 'auto',
      marginStart: 'auto',
      backgroundColor:  '#9ef0d9',

    }
});

export default App;
