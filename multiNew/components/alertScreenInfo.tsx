import React from 'react';
import { StyleSheet , ScrollView} from 'react-native';
import Colors from '../constants/Colors';
import { ExternalLink } from './ExternalLink';
import { MonoText } from './StyledText';
import { Text, View } from './Themed';




export default function EditScreenInfo({ path }: { path: string }) {
  return (
    <ScrollView>
      <View style={styles.getStartedContainer}>
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
                <View style={styles.divider} />
      
        <View style={styles.card}>
              <View style={styles.header}> 
                  <Text style={styles.title2}> 
                      Earthquake Warning
                  </Text> 
              </View> 
              <View style={styles.content}> 
                  <Text style={styles.text}> 
                    Seek shelter! Earthquake Incoming!
                  </Text> 
              </View> 
          </View> 
        </View>
      </View>
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  getStartedContainer: {
    alignItems: 'center',
    marginHorizontal: 50,
    flex: 1,
  },
  card: {
    backgroundColor: 'white',
    borderRadius: 2,
    padding: 16,
    shadowColor: 'black',
    shadowOffset: {
      width: 2,
      height: 2,
    }
    
  },
  divider: {
    borderBottomColor: 'gray',
    borderBottomWidth: 4,
    marginTop: 50,
    marginBottom: 12,
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
  title2: { 
    fontSize: 25  , 
    fontWeight: 'bold', 
    color: 'red', 
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
    borderRadius: 1,
    paddingHorizontal: 2,
  },
  getStartedText: {
    fontSize: 17,
    lineHeight: 24,
    textAlign: 'center',
  },
  
});
