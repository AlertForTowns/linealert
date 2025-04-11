snapshot_schema = {
    "type": "object",
    "properties": {
        "_metadata": {
            "type": "object",
            "properties": {
                "timestamp": {"type": "string"},
                "device_id": {"type": "string"},
                "tool_version": {"type": "string"}
            },
            "required": ["timestamp", "device_id", "tool_version"]
        },
        "detected_protocols": {
            "type": "array",
            "items": {"type": "string"}
        },
        "endpoint_summary": {
            "type": "object",
            "additionalProperties": {
                "type": "object",
                "properties": {
                    "packet_count": {"type": "integer"}
                },
                "required": ["packet_count"]
            }
        },
        "port_activity": {
            "type": "object",
            "additionalProperties": {
                "type": "object",
                "properties": {
                    "TCP": {
                        "type": "array",
                        "items": {"type": "integer"}
                    },
                    "UDP": {
                        "type": "array",
                        "items": {"type": "integer"}
                    }
                },
                "required": ["TCP", "UDP"]
            }
        },
        "protocol_stats": {
            "type": "object",
            "additionalProperties": {
                "type": "object",
                "properties": {
                    "packet_count": {"type": "integer"},
                    "byte_count": {"type": "integer"}
                },
                "required": ["packet_count", "byte_count"]
            }
        },
        "conversations": {
            "type": "object",
            "additionalProperties": {
                "type": "object",
                "properties": {
                    "packet_count": {"type": "integer"}
                },
                "required": ["packet_count"]
            }
        }
    },
    "required": ["_metadata", "detected_protocols", "endpoint_summary", "port_activity", "protocol_stats", "conversations"]
}
