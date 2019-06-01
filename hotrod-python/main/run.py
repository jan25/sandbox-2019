import services.frontend.server as frontend_service
import services.customer.server as customer_service
import services.driver.server as driver_service
import services.route.server as route_service

if __name__ == '__main__':
    frontend_service.start_server()
    customer_service.start_server()
    driver_service.start_server()
    route_service.start_server()