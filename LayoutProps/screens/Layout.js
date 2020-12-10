import React, {useState} from 'react'; //자바스크립트 버전에 따라 리액트 라이브러리에 진입
import {Text, Button, View, StyleSheet, ScrollView} from 'react-native'; //리액트 네이티브 사용
import Constants from 'expo-constants';
import { color } from 'react-native-reanimated';

const Layout = (props) => {
  const {navigation} = props;

  const flexDirections = ['row','row-reverse','column','column-reverse'];
  const justifyContents = [
    'flex-start',
    'flex-end',
    'center',
    'space-between',
    'space-around',
    'space-evenly',
  ];
  const alignItemsArr = [
    'flex-start',
    'flex-end',
    'center',
    'stretch',
    'baseline',
  ];
  const wraps = ['nowrap','wrap','wrap-reverse'];
  const directions = ['inherit','ltr','rtl'];

  const [flexDirection, setFlexDirection] = useState(0);
  const [justifyContent, setjustifyContent] = useState(0);
  const [alignItems, setAlignItems] = useState(0);
  const [direction, setdirection] = useState(0);
  const [wrap, setwrap] = useState(0);

const hookedStyles = {
    flexDirection: flexDirections[flexDirection],
    justifyContent: justifyContents[justifyContent],
    alignItems: alignItemsArr[alignItems],
    direction: directions[direction],
    flexWrap: wraps[wrap],
  };
//추가
  // var p;

  const changeSetting = (value, options, setterFunction) => {
    if (value == options.length - 1) {
      setterFunction(0);
      // p = options[value]; //추가
    } else {
          setterFunction(value + 1); 
          // p = options[value]; //추가
    }
    // p = options[value];
    console.log(options[value]);
  };

  const Square = () => {
    const sqStyle = {
      width: 50,
      height: 50,
      backgroundColor: randomHexColor(),
    };
    return <View style={sqStyle} />;
  };

  const [squares, setSquares] = useState([Square(), Square(), Square()]);

  return (
    <>
      <View style={{ paddingTop: Constants.statusBarHeight}} />
      <View style={[styles.container, styles.playingSpacem, hookedStyles]}>
        {squares.map(elem => elem)}
        
      </View>
      <ScrollView style={[styles.container]}>
        <View style={[styles.controlSpace]}>
          <View style={styles.buttonView}>            
            <Button title="CHANGE FLEX DIRECTION"
              onPress={() => 
                changeSetting(flexDirection, flexDirections, setFlexDirection)
            }/>
            <Text style={{textAlign:"center"}}>{flexDirections[flexDirection]}</Text>
          </View>
          
          <View style={styles.buttonView}>            
            <Button title="CHANGE JUSTIFY CONTENT"
            onPress={() => changeSetting(justifyContent,justifyContents,setjustifyContent)
          }
            />
            <Text style={{textAlign:"center"}}>{justifyContents[justifyContent]}</Text>
          </View>
          <View style={styles.buttonView}>
            <Button title="CHANGE ALIGN ITEMS"
            onPress={() => changeSetting(alignItems, alignItemsArr, setAlignItems)
            }
            />
            <Text style={{textAlign:"center"}}>{alignItemsArr[alignItems]}</Text>
          </View>
          <View style={styles.buttonView}>
            <Button title="CHANGE DIRECTION"
            onPress={() => 
              changeSetting(direction, directions, setdirection)
            }
            />
            <Text style={{textAlign:"center"}}>{directions[direction]}</Text>
          </View>
          <View style={styles.buttonView}>
            <Button title="CHANGE FLEX WRAP"
            onPress={() => 
              changeSetting(wrap, wraps, setwrap)
            }
            />
            <Text style={{textAlign:"center"}}>{wraps[wrap]}</Text>
          </View>
          <View style={styles.buttonView}>
            <Button title="ADD SQUARE"
            onPress={() => 
              setSquares([...squares, Square()])
            }
            />
          </View>
          <View style={styles.buttonView}>
            <Button title="DELETE SQUARE"
            onPress={() => 
              setSquares(squares.filter((v, i) => i != squares.length-1)) /// 뒤에서 부터 지우기
              // i != 0 은 앞에서 부터 지우기
            }
            />
          </View>
          <View style={styles.buttonView}>
            <Button title="Go To Home"
            onPress={() => 
              navigation.navigate('Home')
            }
            />
          </View>
        </View>

      </ScrollView>

    </>

  );
};

const styles = StyleSheet.create({
  container: {
    height: '50%',
  },
  playingSpace: {
    backgroundColor: 'white',
    borderColor: 'blue',
    borderWidth: 3,
  },
  controlSpace: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    backgroundColor: '#F5F5F5',

  },
  buttonView: {
    width: '50%',
    padding: 10,
  }
})

const randomHexColor = () => {
  return '#000000'.replace(/0/g, () => {
    return (~~(Math.random() * 16)).toString(16);
  });
};

export default Layout;