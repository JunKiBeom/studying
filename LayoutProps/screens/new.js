import React from 'react';
import { Image, Text, View, StyleSheet } from 'react-native';
import { color } from 'react-native-reanimated';

function New() {
    return (
        <>
            <Image
                source={require('../assets/dotSky.png')}
                style={{width: 300, height: 400}}
            />
            <Text> Dot SKY</Text>
        </>
    );
}

export default New