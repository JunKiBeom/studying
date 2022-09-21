//
//  ViewController.swift
//  Map
//
//  Created by 전기범 on 2022/09/22.
//

import UIKit
import MapKit

class ViewController: UIViewController,CLLocationManagerDelegate {
    
    let locationManager = CLLocationManager()
    
    @IBOutlet var myMap: MKMapView!
    @IBOutlet var lblLocationInfo1: UILabel!
    @IBOutlet var lblLocationInfo2: UILabel!

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        lblLocationInfo1.text = ""
        lblLocationInfo2.text = ""
        locationManager.delegate = self
        locationManager.desiredAccuracy = kCLLocationAccuracyBest // 정확도를 최고로 설정
        locationManager.requestWhenInUseAuthorization()
        locationManager.startUpdatingLocation()
        myMap.showsUserLocation = true
    }
    
    func goLacation(latitudeValue: CLLocationDegrees, longitudeValue: CLLocationDegrees, delta span :Double) -> CLLocationCoordinate2D {
        let pLocation = CLLocationCoordinate2DMake(latitudeValue, longitudeValue)
        // 위도 경도 값을 매개변수로 하여 CLLocationCoordinate2DMake 함수를 호출, 리턴 값을 pLocation으로 받는다
        
        let spanValue = MKCoordinateSpan(latitudeDelta: span, longitudeDelta: span)
        // 범위 값을 매개변수로 하여 MKCoordinateSpanMake 함수를 호출, 리턴 값을 spanValue로 받는다
        
        let pRegion = MKCoordinateRegion(center: pLocation, span: spanValue)
        // pLocation과 spanValue 값을 매개변수로 하여 MKCoordinateRegionMake 함수를 호출, 리턴 값을 pRegion으로 받는다.
        
        myMap.setRegion(pRegion, animated: true)
        return pLocation
    }
    
    func setAnnitation(latitudeVale: CLLocationDegrees, longitudeValue: CLLocationDegrees, delta span :Double, title strTitle: String, subtitle strSubtitle: String) {
        let annotation = MKPointAnnotation()
        annotation.coordinate = goLacation(latitudeValue: latitudeVale, longitudeValue: longitudeValue, delta: span)
        annotation.title = strTitle
        annotation.subtitle = strSubtitle
        myMap.addAnnotation(annotation)
    }
    
    func locationManager(_ manager: CLLocationManager, didUpdateLocations locations: [CLLocation]) {
        let pLocation = locations.last
        _ = goLacation(latitudeValue: (pLocation?.coordinate.latitude)!, longitudeValue: (pLocation?.coordinate.longitude)!, delta: 0.01)
        CLGeocoder().reverseGeocodeLocation(pLocation!, completionHandler: {
            (placemarks, error) -> Void in
            let pm = placemarks!.first
            let country = pm!.country
            var address: String = country!
            
            if pm!.locality != nil {
                address += " "
                address += pm!.locality!
            }
            
            if pm!.thoroughfare != nil {
                address += " "
                address += pm!.thoroughfare!
            }
            
            self.lblLocationInfo1.text = "현재 위치"
            self.lblLocationInfo2.text = address
        })
        
        locationManager.stopUpdatingLocation()
    }
    @IBAction func sgChangeLocation(_ sender: UISegmentedControl) {
        if sender.selectedSegmentIndex == 0 {
            // 현재 위치 표시
            self.lblLocationInfo1.text = ""
            self.lblLocationInfo2.text = ""
            locationManager.startUpdatingLocation()
        }
        
        else if sender.selectedSegmentIndex == 1 {
            // 폴리텍대학 표시
            setAnnitation(latitudeVale: 37.751853, longitudeValue: 128.8760574000004, delta: 1, title: "한국폴리텍대학 강릉캠퍼스", subtitle: "강원도 강릉시 남산초교길 121")
            self.lblLocationInfo1.text = "보고 계신 위치"
            self.lblLocationInfo2.text = "한국폴리텍대학 강릉캠퍼스"
        }
        
        else if sender.selectedSegmentIndex == 2 {
            // 이지스퍼블리싱 표시
            setAnnitation(latitudeVale: 37.556876, longitudeValue: 126.914066, delta: 1, title: "이지스퍼블리싱", subtitle: "서울시 마포구 잔다리로 109 이지스 빌딩")
            self.lblLocationInfo1.text = "보고 계신 위치"
            self.lblLocationInfo2.text = "이지스퍼블리싱 출판사"
        }
        
        else if sender.selectedSegmentIndex == 3 {
            // 집 표시
            setAnnitation(latitudeVale: 37.591058257389655, longitudeValue: 126.91359916011194, delta: 1, title: "새절역", subtitle: "서울시 은평구 신사동 352-2")
            self.lblLocationInfo1.text = "보고 계신 위치"
            self.lblLocationInfo2.text = "새절역"
        }
    }

}

