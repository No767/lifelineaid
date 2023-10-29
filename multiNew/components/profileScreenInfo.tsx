import React from 'react';
import { StyleSheet, Image } from 'react-native';

import { Text, View } from './Themed';

export default function EditScreenInfo({path} : {path: string}) {
  return (
    <View style={styles.container}>
      <Text style={styles.username}>@benitezashly</Text>
      
      <Image style={styles.profileImage} source={{uri: '/Users/javi/Desktop/hackathons/calhacks23/lifelineaid/multiNew/assets/images/icon.png'}} />
      
      <Text style={styles.header}>Account Setting:</Text>
      <Text style={styles.item}>Password</Text>
      <Text style={styles.item}>Personal Information</Text>
      <Text style={styles.item}>Verification</Text>
      
      <Text style={styles.header}>Medical Information</Text>
      <Text style={styles.item}>Emergency Contact</Text>
      <Text style={styles.item}>Medication</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    padding: 20,
  },
  username: {
    fontSize: 24,
    fontWeight: 'bold',
    textAlign: 'center',
    marginBottom: 20,
  },
  profileImage: {
    width: 100,
    height: 100,
    borderRadius: 50,
    alignSelf: 'center',
    marginBottom: 20,
  },
  header: {
    fontSize: 20,
    fontWeight: 'bold',
    marginTop: 20,
  },
  item: {
    fontSize: 16,
    paddingVertical: 8,
  },
});
