import * as React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';

import Layout from "../screens/Layout"
import Home from "../screens/home"
<<<<<<< HEAD
import New from "../screens/new"
=======
>>>>>>> 57c655653d0bce68dfc09b06597459e2488eb4b4

const Nav = createStackNavigator();

function MainStackNavigator() {
    return (
        <NavigationContainer>
<<<<<<< HEAD
            <Nav.Navigator 
                initialRouteName='Home'
            >
                <Nav.Screen 
                    name = "Home" 
                    component={Home} 
                    options = {{title : 'home screen'}}/>

                <Nav.Screen 
                    name = "Layout" 
                    component = {Layout} 
                    options={{ title: 'layout Screen'}}/>

                <Nav.Screen
                    name = "new"
                    component = {New}
                    options={{title: 'New Screen'}}
                />
                
            </Nav.Navigator>
=======
            <Stack.Navigator 
                initialRouteName='Home'
            >
                <Stack.Screen name = "Home" component={Home} options = {{title : 'home screen'}}/>
                <Stack.Screen name = "Layout" component = {Layout} options={{ title: 'layout Screen'}}/>
            </Stack.Navigator>
>>>>>>> 57c655653d0bce68dfc09b06597459e2488eb4b4
        </NavigationContainer>

    )
}

export default MainStackNavigator