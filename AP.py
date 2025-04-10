import os
import time
import shutil
import win32print
import win32api
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import logging


logging.basicConfig(level=logging.DEBUG)


folder_to_monitor = r'file_path'
destination_folder = r'file_path' 

os.makedirs(destination_folder, exist_ok=True)

 
printer_name = win32print.GetDefaultPrinter()

class PrintHandler(FileSystemEventHandler):
    def on_created(self, event):
        logging.info(f"File created event: {event.src_path}")
        self.process(event)

    def on_modified(self, event):
        logging.info(f"File modified event: {event.src_path}")
        self.process(event)

    def process(self, event):
       
        if not event.is_directory and event.src_path.lower().endswith('.pdf'):
            filepath = event.src_path
            logging.info(f"Processing file: {filepath}")
          
            time.sleep(5)  
            self.copy_pdf(filepath)

    def copy_pdf(self, filepath):
        try:
            
            destination_path = os.path.join(destination_folder, os.path.basename(filepath))
           
            shutil.copy2(filepath, destination_path)
            logging.info(f"Copied {filepath} to {destination_path}")
            
            self.print_pdf(destination_path)
        except Exception as e:
            logging.error(f"Failed to copy {filepath} to {destination_folder}: {e}")

    def print_pdf(self, filepath):
        try:
          
            adobe_path = r"adobe_path"
        
          
            attempts = 3
            for attempt in range(attempts):
                try:
                    if os.path.exists(adobe_path):
                        
                        logging.info(f"Printing {filepath} using Adobe Reader (attempt {attempt + 1}).")
                        win32api.ShellExecute(0, "open", adobe_path, f'/s /o /h /t "{filepath}" "{printer_name}"', None, 1)
                    else:
                       
                        logging.warning(f"Adobe Reader not found. Printing {filepath} using the default PDF handler (attempt {attempt + 1}).")
                        win32api.ShellExecute(0, "print", filepath, None, ".", 0)
                
                
                    time.sleep(5)
                    break  
                except Exception as e:
                    logging.error(f"Attempt {attempt + 1} failed to print {filepath}: {e}")
                    if attempt < attempts - 1:
                        logging.info("Retrying printing...")
                        time.sleep(2)
                    else:
                        logging.error(f"Failed to print {filepath} after {attempts} attempts.")
        except Exception as e:
            logging.error(f"Failed to print {filepath}: {e}")
    

if __name__ == "__main__":
  
    event_handler = PrintHandler()
    observer = Observer()
  
    observer.schedule(event_handler, path=folder_to_monitor, recursive=False)
    observer.start()

    try:
        
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
      
        observer.stop()
    observer.join()
