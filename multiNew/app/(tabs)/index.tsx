import { StyleSheet } from 'react-native';
import EditScreenInfo from '../../components/mainScreenInfo';
import { Text, View } from '../../components/Themed';
import React, { useState } from 'react';
//Map Imports
import MapView, { PROVIDER_GOOGLE } from "react-native-maps";
import {Marker} from 'react-native-maps';


export default function TabOneScreen() {


  return (
    
    <View style={styles.container}>
      <Text style={styles.title}>Maps</Text>
        <MapView 
          provider={PROVIDER_GOOGLE} // Specify Google Maps as the provider
          initialRegion={{
            latitude: 31.189365713577544,
            longitude: 34.81192547178498,
            latitudeDelta: 2.2922,
            longitudeDelta: 2.2421,
          }}
          style={styles.map} >
            <Marker
              coordinate={{ latitude: 31.41856120169955, longitude: 34.78162222467485}}
              title="Wildfire"
              description="Wild fire occuring in Israel. Stay Safe and Avoid Area"
              pinColor="red"
            />
            <Marker
              coordinate={{ latitude: 30.41856120169955, longitude: 35.48162222467485}}
              title="Medical Aid"
              description="Medical Aid provided by blah blah blah organization"
              pinColor="green"
            />
            <Marker
              coordinate={{ latitude:  31.5385, longitude: 34.5368}}
              title="Bombing" 
              description="Stay Away. Area in Critical Condition"
              pinColor="red"
            />
            <Marker
              coordinate={{ latitude:  31.448182743953613, longitude: 34.40736930256567}}
              title="Fire"
              description="Vehicle fire. Stay Cautious"
              pinColor="red"
            />
        </MapView>
        
      <View style={styles.separator} lightColor="#eee" darkColor="rgba(255,255,255,0.1)" />
      <EditScreenInfo path="app/(tabs)/index.tsx" />
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
    marginVertical: 30,
    height: 1,
    width: '80%',
  },
  map: {
    width: '100%',
    height: '100%',
  },
});
