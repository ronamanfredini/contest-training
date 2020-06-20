types = { SETUP: 0, TRANSFER: 1, SUCCESS: 2, ERROR: 3 };

class BaseMessage {
    type;
    message;
    originalSender;
    actualSender;
    target;
}


exports.BaseMessage = BaseMessage;
exports.MessageTypes = types;