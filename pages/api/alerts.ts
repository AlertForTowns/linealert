import fs from 'fs';
import path from 'path';
import type { NextApiRequest, NextApiResponse } from 'next';

export default function handler(req: NextApiRequest, res: NextApiResponse) {
  const alertsDir = path.join(process.cwd(), 'alerts');
  const alertFile = path.join(alertsDir, 'alert_log.jsonl');

  try {
    const content = fs.readFileSync(alertFile, 'utf-8');
    const lines = content.trim().split('\n');
    const alerts = lines.map(line => JSON.parse(line));
    res.status(200).json({ alerts });
  } catch (error) {
    console.error('Failed to parse alerts:', error);
    res.status(500).json({ error: 'Failed to load alerts.' });
  }
}
