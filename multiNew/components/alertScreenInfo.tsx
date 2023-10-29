import React from 'react';
import { StyleSheet } from 'react-native';
import Colors from '../constants/Colors';
import { ExternalLink } from './ExternalLink';
import { MonoText } from './StyledText';
import { Text, View } from './Themed';




export default function EditScreenInfo({ path }: { path: string }) {
  return (
    <View>
      <View style={styles.card}>
        
              
              <View style={styles.header}> 
                  <Text style={styles.title}> 
                      Medical Center at Shansha
                  </Text> 
              </View> 

              <View style={styles.content}> 
                  <Text style={styles.text}> 
                    Can supply first aid care, shelter, medicine, and relay to rescue organizations
                  </Text> 
              </View> 
              
      <View/>
      
      <View style={styles.card}>
              <View style={styles.header}> 
                  <Text style={styles.title}> 
                      Medical Center at Shansha
                  </Text> 
              </View> 
                
              <View style={styles.content}> 
                  <Text style={styles.text}> 
                    Can supply first aid care, shelter, medicine, and relay to rescue organizations
                  </Text> 
              </View> 
          </View> 
        </View>
       
    </View>
  );
}

const styles = StyleSheet.create({
  getStartedContainer: {
    alignItems: 'center',
    marginHorizontal: 50,
  },
  card: {
    backgroundColor: 'white',
    borderRadius: 15,
    padding: 16,
    shadowColor: 'black',
    shadowOffset: {
      width: 0,
      height: 4,
    }
  },
  header: { 
    marginBottom: 16, 
    alignItems: 'center', 
  }, 
  title: { 
    fontSize: 25  , 
    fontWeight: 'bold', 
    color: 'green', 
  }, 
  subtitle: { 
    fontSize: 24, 
    color: '#333', 
    marginTop: 10, 
  }, 
  content: { 
    alignItems: 'center', 
  }, 
  text: { 
    fontSize: 17, 
    color: '#444444', 
    textAlign: 'center', 
  }, 
  homeScreenFilename: {
    marginVertical: 7,
  },
  codeHighlightContainer: {
    borderRadius: 3,
    paddingHorizontal: 4,
  },
  getStartedText: {
    fontSize: 17,
    lineHeight: 24,
    textAlign: 'center',
  },
  
});
