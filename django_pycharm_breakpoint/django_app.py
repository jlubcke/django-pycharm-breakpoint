import sys
import threading

from django.apps import AppConfig
from django.conf import settings
from django.core.handlers import exception


class DjangoPycharmBreakpointConfig(AppConfig):
    name = 'django_pycharm_breakpoint'
    verbose_name = 'Django PyCharm breakpoint'

    def ready(self):
        if not settings.DEBUG:
            return

        original_response_for_exception = exception.response_for_exception

        def monkey_patched_response_for_exception(request, exc):
            breakpoint_on_exception()
            return original_response_for_exception(request, exc)

        exception.response_for_exception = monkey_patched_response_for_exception

        try:
            import rest_framework
            from rest_framework.views import APIView
        except ImportError:
            pass
        else:
            APIView.original_handle_exception = APIView.handle_exception

            def monkey_patched_handle_exception(self, exc):
                breakpoint_on_exception()
                return self.original_handle_exception(exc)

            APIView.handle_exception = monkey_patched_handle_exception


def breakpoint_on_exception():
    try:
        import pydevd
        from pydevd import pydevd_tracing
    except ImportError:
        pass
    else:
        exctype, value, traceback = sys.exc_info()
        frames = []
        while traceback:
            frames.append(traceback.tb_frame)
            traceback = traceback.tb_next
        thread = threading.current_thread()
        frames_by_id = dict([(id(frame), frame) for frame in frames])
        frame = frames[-1]
        if hasattr(thread, "additional_info"):
            thread.additional_info.pydev_message = "Uncaught exception"
        try:
            debugger = pydevd.debugger
        except AttributeError:
            debugger = pydevd.get_global_debugger()
        pydevd_tracing.SetTrace(None)  # no tracing from here
        debugger.stop_on_unhandled_exception(thread, frame, frames_by_id, (exctype, value, traceback))

