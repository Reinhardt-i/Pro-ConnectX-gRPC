import grpc
from concurrent import futures
import proconnectx_pb2
import proconnectx_pb2_grpc
import logging


_USERS = {}
_USER_PROFILES = {}  # New dictionary to store user profiles


class ProConnectXServicer(proconnectx_pb2_grpc.ProConnectXServicer):

    # Existing methods (Register and Login) go here...

    def SetProfile(self, request, context):
        user_id = request.user_id
        profile_data = request.profile_data

        try:
            _USER_PROFILES[user_id] = profile_data
            return proconnectx_pb2.ProfileResponse(success=True, message="Profile updated successfully.")
        except Exception as e:
            logging.error(f"SetProfile error: {str(e)}")
            return proconnectx_pb2.ProfileResponse(success=False, message="Failed to update profile.")

    def GetProfile(self, request, context):
        user_id = request.user_id

        try:
            if user_id in _USER_PROFILES:
                profile_data = _USER_PROFILES[user_id]
                return proconnectx_pb2.GetProfileResponse(success=True, profile_data=profile_data, message="Profile retrieved successfully.")
            else:
                return proconnectx_pb2.GetProfileResponse(success=False, message="Profile not found.")
        except Exception as e:
            logging.error(f"GetProfile error: {str(e)}")
            return proconnectx_pb2.GetProfileResponse(success=False, message="Failed to retrieve profile.")

    def UpdateProfile(self, request, context):
        user_id = request.user_id
        updated_data = request.updated_data

        try:
            if user_id in _USER_PROFILES:
                _USER_PROFILES[user_id] = updated_data
                return proconnectx_pb2.UpdateProfileResponse(success=True, message="Profile updated successfully.")
            else:
                return proconnectx_pb2.UpdateProfileResponse(success=False, message="Profile not found.")
        except Exception as e:
            logging.error(f"UpdateProfile error: {str(e)}")
            return proconnectx_pb2.UpdateProfileResponse(success=False, message="Failed to update profile.")

