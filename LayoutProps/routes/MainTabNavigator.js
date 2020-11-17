import * as React from 'react';
import {NavigationContainer} from '@react-navigation/native';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';

import Layout from "../screens/Layout"
import Home from "../screens/home"
import New from "../screens/new"

const Nav = createBottomTabNavigator();

function MainTabNavigator() {
    return(
        <NavigationContainer>
            <Nav.Navigator initialRouteName='Home' >
                <Nav.Screen 
                    name = "Home" 
                    component = {Home} 
                    options={{ title: 'home screen'}} 
                />

                <Nav.Screen 
                    name = "Layout" 
                    component = {Layout} 
                    options={{ title: 'layout screen'}} 
                />

                <Nav.Screen
                    name = "new"
                    component = {New}
                    options={{title: 'New Screen'}}
                />

            </Nav.Navigator>
        </NavigationContainer>
    )
}

export default MainTabNavigator