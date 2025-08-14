# Import Libraries
import pandas as pd


# Define bandit training function
def train_bandit(bandit, events, user_features, n_users=None, stats_interval=500):
    """
    Full training with tracking
    
    Args:
        bandit: Pre-initialized MarketingBandit
        events: Processed events DataFrame
        user_features: User features DataFrame
        n_users: Max users to process (None for all)
        stats_interval: Log stats every N users
    
    Returns:
        Tuple: (trained_bandit, stats_history)
    """
    stats_history = []
    user_ids = events['visitorid'].unique()
    
    # Filter train users if n_users specified
    if n_users is not None:
        user_ids = user_ids[:n_users]
    
    for i, visitor_id in enumerate(user_ids, 1):
        group = events[events['visitorid'] == visitor_id]
        user_feats = user_features.loc[visitor_id].to_dict()
        
        # Process view events
        view_events = group[group['event'] == 'view']
        for _, session in view_events.iterrows():
            context = {
                'hour': session['hour'],
                'is_weekend': session['is_weekend'],
                'item_price': session['price'],
                'item_category': session['category']
            }
            
            action = bandit.select_action(user_feats, context)
            
            # Calculate reward
            next_4h = (group['timestamp'] > session['timestamp']) & \
                      (group['timestamp'] < session['timestamp'] + pd.Timedelta(hours=4))
            reward = int('transaction' in group[next_4h]['event'].values)
            
            bandit.update(user_feats, context, action, reward)
        
        # Log statistics periodically
        if i % stats_interval == 0:
            stats = bandit.get_action_stats()
            stats['users_processed'] = i
            stats_history.append(stats)
            print(f"Processed {i}/{len(user_ids)} users")
    
    return bandit, pd.concat(stats_history) if stats_history else None