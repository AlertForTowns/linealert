from scapy.all import sniff
from asset_discovery import AssetInventory
import logging

# Initialize the asset inventory and configure logging
inventory = AssetInventory()

# Set up basic logging for the main process
logging.basicConfig(filename='linealert.log', level=logging.INFO)

def handle_packet(packet):
    """
    Process each packet, update the asset inventory, and handle logging and alerts.
    """
    # Update inventory with information from the packet
    inventory.update_from_packet(packet)

    # Log significant events: new device detection
    if packet[IP].src not in inventory.assets:
        logging.info(f"New device discovered: {packet[IP].src} at {datetime.utcnow().isoformat()}")

    # Print the current asset inventory every time (for debugging purposes)
    inventory.print_inventory()

def start_sniffing(interface):
    """
    Start sniffing on the given interface for packets.
    """
    try:
        logging.info(f"Starting packet capture on {interface}")
        sniff(iface=interface, prn=handle_packet, store=False)
    except Exception as e:
        logging.error(f"Error while sniffing: {str(e)}")

def main():
    """
    Main function to initialize asset discovery and start monitoring.
    """
    interface = "eth0"  # Example interface, modify as needed
    logging.info("Starting LineAlert monitoring system...")
    
    # Load previous asset inventory if available
    inventory.load_from_file('assets.json')
    
    # Start sniffing network traffic
    start_sniffing(interface)
    
    # Save inventory to file periodically (or based on events)
    inventory.save_to_file('assets.json')

if __name__ == "__main__":
    main()
