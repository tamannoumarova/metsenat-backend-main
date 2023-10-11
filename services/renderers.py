from rest_framework.renderers import JSONRenderer


class CustomRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        status_code = renderer_context["response"].status_code
        response = {"status": "success", "message": None, "data": data}

        if not str(status_code).startswith("2"):
            response["status"] = "error"
            response["data"] = None
            errors = {}
            error_messages = data.get("messages")
            if not error_messages:
                for key, value in data.items():
                    if (isinstance(value, str) or isinstance(value, list)) and len(value) > 0:
                        if isinstance(value, str):
                            errors = str(value)
                            break
                        else:
                            errors[key] = [str(error) for error in value]

                if errors:
                    response["message"] = list(errors.values())[0][0] if isinstance(errors, dict) else errors
                else:
                    response["message"] = None
            elif error_messages[0] and error_messages[0].get("message"):
                response["message"] = error_messages[0].get("message")
            else:
                response["message"] = None

        return super().render(response, accepted_media_type, renderer_context)
