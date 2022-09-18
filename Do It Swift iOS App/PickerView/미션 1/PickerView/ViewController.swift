//
//  ViewController.swift
//  PickerView
//
//  Created by 전기범 on 2022/09/18.
//

import UIKit

class ViewController: UIViewController,UIPickerViewDelegate, UIPickerViewDataSource {
    
    let MAX_ARRAY_NUM = 10
    let PICKER_VIEW_COLUMM = 2
    let PICKER_VIEW_HEIGHT : CGFloat = 80
    var imageArray = [UIImage?]()
    var imageFileName : [String] = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg", "6.jpg", "7.jpg", "8.jpg", "9.jpg", "10.jpg"]
    
    @IBOutlet var pickerImage: UIPickerView!
    @IBOutlet var lblImageFileName: UILabel!
    @IBOutlet var imageView: UIImageView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        
        for i in 0 ..< MAX_ARRAY_NUM {
            let image = UIImage(named: imageFileName[i])
            imageArray.append(image)
        }
        
        lblImageFileName.text = imageFileName[0]
        imageView.image = imageArray[0]
    }
    func numberOfComponents(in pickerView: UIPickerView) -> Int {
        return PICKER_VIEW_COLUMM
    } // PickerView에게 Component의 수를 정수 값으로 넘겨주는 Delegate Method,표시되는 열의 개수 의미 {여기서는 1}
    
    func pickerView(_ pickerView: UIPickerView, numberOfRowsInComponent component: Int) -> Int {
        return imageFileName.count
    } // numberOfRowsInComponent 인수를 가지는 Delegate Method, 열의 개수를 정수 값으로 넘겨줌 PickerView의 해당 열에서 선택할 수 있는 행의 개수(데이터의 개수)를 의미 {여기서는 10}
    
//    func pickerView(_ pickerView: UIPickerView, titleForRow row: Int, forComponent component: Int) -> String? {
//        return imageFileName[row]
//    }  // titleForRow 인수를 가지는 Delegate Method, PickerView에게 Component의 각 열의 타이틀 문자열 값으로 넘겨줌 {여기서는 파일명}
    
    func pickerView(_ pickerView: UIPickerView, viewForRow row: Int, forComponent component: Int, reusing view: UIView?) -> UIView {
        let imageView = UIImageView(image: imageArray[row])
        imageView.frame = CGRect(x:0, y:0, width: 100, height: 150)
        
        return imageView
    }
    
    func pickerView(_ pickerView: UIPickerView, rowHeightForComponent component: Int) -> CGFloat {
        return PICKER_VIEW_HEIGHT
    }
    
    func pickerView(_ pickerView: UIPickerView, didSelectRow row: Int, inComponent component: Int) {
        lblImageFileName.text = imageFileName[row]
        imageView.image = imageArray[row]
    }  // 사용자가 PickerView의 룰렛에서 선택한 row 값을 사용하여 imageFileName배열에서 row값에 해당하는 문자열을 가져와 레이블의 Outlet변수인 lblImageFileName.text에 저장

}

