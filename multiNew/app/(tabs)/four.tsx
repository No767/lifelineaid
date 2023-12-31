import { StyleSheet } from 'react-native';
import React from 'react';
import EditScreenInfo from '../../components/profileScreenInfo';
import { Text, View } from '../../components/Themed';


export default function TabFourScreen() {
  return (
    <View style={styles.container}>
     
      <View style={styles.separator} lightColor="#eee" darkColor="rgba(255,255,255,0.1)" />
      <EditScreenInfo path="app/(tabs)/four.tsx" />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
  },
  title: {
    fontSize: 20,
    fontWeight: 'bold',
  },
  separator: {
    marginVertical: 5,
    height: 1,
    width: '80%',
    
  },
});
