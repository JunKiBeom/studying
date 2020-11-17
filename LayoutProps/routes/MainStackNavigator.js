import * as React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';

import Layout from "../screens/Layout"
import Home from "../screens/home"

const Stack = createStackNavigator();

function MainStackNavigator() {
    return (
        <NavigationContainer>
            <Stack.Navigator 
                initialRouteName='Home'
            >
                <Stack.Screen name = "Home" component={Home} options = {{title : 'home screen'}}/>
                <Stack.Screen name = "Layout" component = {Layout} options={{ title: 'layout Screen'}}/>
            </Stack.Navigator>
        </NavigationContainer>

    )
}

export default MainStackNavigator