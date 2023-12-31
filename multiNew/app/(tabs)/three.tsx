import { StyleSheet } from 'react-native';
import React from 'react';
import EditScreenInfo from '../../components/contactScreenInfo';
import { Text, View } from '../../components/Themed';

export default function TabThreeScreen() {
  return (
    <View style={styles.container}>
      
      <View style={styles.separator} lightColor="#eee" darkColor="rgba(255,255,255,0.1)" />
      <EditScreenInfo path="app/(tabs)/three.tsx" />
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
    marginVertical: 10,
    height: 1,
    width: '80%',
  },
});
