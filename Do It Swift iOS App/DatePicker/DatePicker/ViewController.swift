//
//  ViewController.swift
//  DatePicker
//
//  Created by 전기범 on 2022/09/16.
//

import UIKit

class ViewController: UIViewController {
    
    let timeSelector : Selector = #selector(ViewController.updateTime)    // 타이머가 구동되면 실행할 함수 지정
    let interval = 1.0    // 타이머의 간격 값
    var count = 0    // 타이머가 설정한 간격대로 실행되는지 확인하기 위한 변수
    var alarmT : String?
    
    @IBOutlet var lblCurrentTime: UILabel!
    @IBOutlet var lblPickerTime: UILabel!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        
        Timer.scheduledTimer(timeInterval: interval, target: self, selector: timeSelector, userInfo: nil, repeats: true)
    }

    @IBAction func changeDatePicker(_ sender: UIDatePicker) {
        let datePickerView = sender
        
        let formatter = DateFormatter()
        formatter.dateFormat = "yyyy-MM-dd HH:mm EEE"
        lblPickerTime.text = "선택시간 : " + formatter.string(from: datePickerView.date)
        
        formatter.dateFormat = "hh:mm aaa"
        alarmT = formatter.string(from: datePickerView.date)
    }
    
    @objc func updateTime() {
        /*
        lblCurrentTime.text = String(count)
        count+=1
        */
        let date = NSDate()
        
        let formatter = DateFormatter()
        formatter.dateFormat = "yyyy-MM-dd HH:mm EEE"
        lblCurrentTime.text = "현재시간 : " + formatter.string(from: date as Date)
        // 피커 뷰에서 선택한 날짜를 formatter의 dateFormat에서 설정한 포맷대로 string메서드를 사용하여 문자열로 변환.
        // lblCurrentTime.text -> String에 위에서 String으로 변환한 date값을 추가하여 lblCurrentTime의 text에 넣음
        
        formatter.dateFormat = "hh:mm aaa"
        let currentT = formatter.string(from: date as Date)
        
        if (alarmT==currentT){
            view.backgroundColor = UIColor.red
        }
        else {
            view.backgroundColor = UIColor.white
        }
    }
}

