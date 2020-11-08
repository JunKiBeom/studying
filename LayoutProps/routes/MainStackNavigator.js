import * as React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';

import Layout from "../screens/Layout"

const Stack = createStackNavigator();

function MainStackNavigator() {
    return (
        <NavigationContainer>
            <Stack.Navigator 
                initialRouteName='Layout'
            >
                <Stack.Screen 
                    name = "Layout"
                    component = {Layout}
                    options={{ title: 'layout Screen'}}
                />
            </Stack.Navigator>
        </NavigationContainer>

    )
}

export default MainStackNavigator