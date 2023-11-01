#add this lines to configuration.yaml
sensor: 
  - platform: hibouair_ble
    scan_interval: 120

#Sample Entities Card configuration
type: entities
entities:
  - entity: sensor.hibouair_ble_co2
  - entity: sensor.hibouair_ble_temperature
  - entity: sensor.hibouair_ble_humidity
  - entity: sensor.hibouair_ble_light
  - entity: sensor.hibouair_ble_pm1
  - entity: sensor.hibouair_ble_pm2_5
  - entity: sensor.hibouair_ble_pm10
  - entity: sensor.hibouair_ble_pressure
  - entity: sensor.hibouair_ble_voc
  - entity: sensor.hibouair_ble_last_updated
header:
  type: picture
  image: https://www.hibouair.com/blog/wp-content/uploads/2023/10/hibouair_banner_ble.jpg
  tap_action:
    action: none
  hold_action:
    action: none


