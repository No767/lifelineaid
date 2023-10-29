import React from 'react';
import { StyleSheet, TouchableOpacity, ScrollView } from 'react-native';

import Colors from '../constants/Colors';
import { Text, View } from './Themed';

export default function EditScreenInfo({path} : {path: string}) {
  return (
    <ScrollView>
    <View style={styles.container}>

      <TouchableOpacity style={styles.emergencyButton} onPress={() => {}}>
        <Text style={styles.emergencyButtonText}>Need Urgent Help? Tap Here</Text>
      </TouchableOpacity>

      <View style={styles.card}>
        <Text style={styles.cardTitle}>Local Organizations</Text>
        <Text style={styles.cardDescription}>Largest humanitarian aid organization in Israel</Text>
        <TouchableOpacity style={styles.actionButton} onPress={() => {}}>
          <Text style={styles.actionButtonText}>Contact</Text>
        </TouchableOpacity>
      </View>

      <View style={styles.card}>
        <Text style={styles.cardTitle}>Government Agencies</Text>
        <Text style={styles.cardDescription}>Largest humanitarian aid organization in Israel</Text>
        <TouchableOpacity style={styles.actionButton} onPress={() => {}}>
          <Text style={styles.actionButtonText}>Contact</Text>
        </TouchableOpacity>
      </View>

      <View style={styles.card}>
        <Text style={styles.cardTitle}>Israel</Text>
        <Text style={styles.cardDescription}>Largest humanitarian aid organization in Israel</Text>
        <TouchableOpacity style={styles.actionButton} onPress={() => {}}>
          <Text style={styles.actionButtonText}>Contact</Text>
        </TouchableOpacity>
      </View>

      {/* ... Add other cards similarly ... */}

    </View>
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: 'D6CCC2',
    paddingHorizontal: 20,
    paddingTop: 1,
  },
  emergencyButton: {
    backgroundColor: 'red',
    padding: 20,
    borderRadius: 10,
    marginBottom: 20,
    alignItems: 'flex-start',
  },
  emergencyButtonText: {
    color: 'white',
    fontWeight: 'bold',
    fontSize: 20,
  },
  card: {
    backgroundColor: 'grey',
    padding: 20,
    borderRadius: 10,
    marginBottom: 20,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 5,
    elevation: 3,
  },
  cardTitle: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 10,
  },
  cardDescription: {
    fontSize: 18,
    color: 'white',
    marginBottom: 20,
  },
  actionButton: {
    backgroundColor: 'blue',
    padding: 15,
    borderRadius: 8,
    alignItems: 'center',
  },
  actionButtonText: {
    color: 'white',
    fontWeight: 'bold',
    fontSize: 18,
  },
});

