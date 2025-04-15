import fs from 'fs';
import path from 'path';
import type { NextApiRequest, NextApiResponse } from 'next';

export default function handler(req: NextApiRequest, res: NextApiResponse) {
  const alertsDir = path.join(process.cwd(), 'alerts');

  try {
    const alertFiles = fs.readdirSync(alertsDir);
    const alerts = alertFiles
      .filter((file) => file.endsWith('.json'))
      .map((file) => {
        const content = fs.readFileSync(path.join(alertsDir, file), 'utf-8');
        try {
          const parsed = JSON.parse(content);
          return parsed.message || JSON.stringify(parsed);
        } catch {
          return content;
        }
      });

    res.status(200).json({ alerts });
  } catch (error) {
    res.status(500).json({ error: 'Failed to load alerts.' });
  }
}
