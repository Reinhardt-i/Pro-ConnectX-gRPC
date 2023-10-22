import grpc
import proconnectx_pb2
import proconnectx_pb2_grpc
import logging


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = proconnectx_pb2_grpc.ProConnectXStub(channel)
        
        # Registration
        registration_request = proconnectx_pb2.RegistrationRequest(username="test", password="password")
        try:
            registration_response = stub.Register(registration_request)
            logging.info("Registration Status: %s %s", registration_response.success, registration_response.message)
        except Exception as e:
            logging.error("Registration error: %s", str(e))

        # Login
        login_request = proconnectx_pb2.LoginRequest(username="test", password="password")
        try:
            login_response = stub.Login(login_request)
            logging.info("Login Status: %s %s %s", login_response.success, login_response.message, login_response.user_id)
        except Exception as e:
            logging.error("Login error: %s", str(e))

        # Set Profile
        set_profile_request = proconnectx_pb2.ProfileRequest(user_id=login_response.user_id, profile_data="Sample profile data")
        try:
            set_profile_response = stub.SetProfile(set_profile_request)
            logging.info("Set Profile Status: %s %s", set_profile_response.success, set_profile_response.message)
        except Exception as e:
            logging.error("Set Profile error: %s", str(e))

        # Get Profile
        get_profile_request = proconnectx_pb2.GetProfileRequest(user_id=login_response.user_id)
        try:
            get_profile_response = stub.GetProfile(get_profile_request)
            if get_profile_response.success:
                logging.info("Get Profile Status: Profile data: %s", get_profile_response.profile_data)
            else:
                logging.error("Get Profile error: %s", get_profile_response.message)
        except Exception as e:
            logging.error("Get Profile error: %s", str(e))

        # Update Profile
        update_profile_request = proconnectx_pb2.UpdateProfileRequest(user_id=login_response.user_id, updated_data="Updated profile data")
        try:
            update_profile_response = stub.UpdateProfile(update_profile_request)
            logging.info("Update Profile Status: %s %s", update_profile_response.success, update_profile_response.message)
        except Exception as e:
            logging.error("Update Profile error: %s", str(e))


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    run()
