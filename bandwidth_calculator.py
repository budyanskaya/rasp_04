def calculate_bandwidth(gossip_interval, gossip_fanout, nodes, packet_loss_pct, node_failures_pct):
    PACKET_SIZE_BYTES = 1024
    OVERHEAD_FACTOR = 1.2
    active_nodes = nodes * (1 - node_failures_pct / 100)
    messages_per_second = (1 / gossip_interval) * gossip_fanout * active_nodes
    effective_messages = messages_per_second * (1 - packet_loss_pct / 100)
    data_per_second_bytes = effective_messages * PACKET_SIZE_BYTES * OVERHEAD_FACTOR
    return data_per_second_bytes * 8