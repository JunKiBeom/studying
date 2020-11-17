import React from 'react';
import { Image, Text, View, StyleSheet, Button, TouchableOpacity } from 'react-native';

function Home({navigation}) {
    return (
        <View style={styles.container}> 
            <Image
                source={require('../assets/frog-1371919.png')}
                style={{width: 400, height: 400}}
            />
            <TouchableOpacity
                style={styles.buttonContainer}
                onPress={() => navigation.navigate('Layout')}
            >

                <Text style={styles.buttonText}>Go To Layout</Text>
            </TouchableOpacity>

            <Button
                title="Go to New Screen"
                onPress={() => navigation.navigate('new')} 
            />
        </View>
    );
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center',
        backgroundColor: '#ebebeb'

    },

    buttonContainer:{
        backgroundColor: 'black',
        borderRadius: 5,
        padding: 10,
        margin: 20
    },
    buttonText: {
        fontSize: 20,
        color: '#fff'

    }
})

export default Home