
'Client and server classes corresponding to protobuf-defined services.'
import grpc
from ....cosmos.bank.v1beta1 import tx_pb2 as cosmos_dot_bank_dot_v1beta1_dot_tx__pb2

class MsgStub(object):
    'Msg defines the bank Msg service.\n    '

    def __init__(self, channel):
        'Constructor.\n\n        Args:\n            channel: A grpc.Channel.\n        '
        self.Send = channel.unary_unary('/cosmos.bank.v1beta1.Msg/Send', request_serializer=cosmos_dot_bank_dot_v1beta1_dot_tx__pb2.MsgSend.SerializeToString, response_deserializer=cosmos_dot_bank_dot_v1beta1_dot_tx__pb2.MsgSendResponse.FromString)
        self.MultiSend = channel.unary_unary('/cosmos.bank.v1beta1.Msg/MultiSend', request_serializer=cosmos_dot_bank_dot_v1beta1_dot_tx__pb2.MsgMultiSend.SerializeToString, response_deserializer=cosmos_dot_bank_dot_v1beta1_dot_tx__pb2.MsgMultiSendResponse.FromString)

class MsgServicer(object):
    'Msg defines the bank Msg service.\n    '

    def Send(self, request, context):
        'Send defines a method for sending coins from one account to another account.\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MultiSend(self, request, context):
        'MultiSend defines a method for sending coins from some accounts to other accounts.\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_MsgServicer_to_server(servicer, server):
    rpc_method_handlers = {'Send': grpc.unary_unary_rpc_method_handler(servicer.Send, request_deserializer=cosmos_dot_bank_dot_v1beta1_dot_tx__pb2.MsgSend.FromString, response_serializer=cosmos_dot_bank_dot_v1beta1_dot_tx__pb2.MsgSendResponse.SerializeToString), 'MultiSend': grpc.unary_unary_rpc_method_handler(servicer.MultiSend, request_deserializer=cosmos_dot_bank_dot_v1beta1_dot_tx__pb2.MsgMultiSend.FromString, response_serializer=cosmos_dot_bank_dot_v1beta1_dot_tx__pb2.MsgMultiSendResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('cosmos.bank.v1beta1.Msg', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class Msg(object):
    'Msg defines the bank Msg service.\n    '

    @staticmethod
    def Send(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.bank.v1beta1.Msg/Send', cosmos_dot_bank_dot_v1beta1_dot_tx__pb2.MsgSend.SerializeToString, cosmos_dot_bank_dot_v1beta1_dot_tx__pb2.MsgSendResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MultiSend(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.bank.v1beta1.Msg/MultiSend', cosmos_dot_bank_dot_v1beta1_dot_tx__pb2.MsgMultiSend.SerializeToString, cosmos_dot_bank_dot_v1beta1_dot_tx__pb2.MsgMultiSendResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
