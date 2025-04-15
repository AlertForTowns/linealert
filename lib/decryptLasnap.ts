import * as crypto from 'crypto';

export function decryptLasnap(buffer: Buffer): string {
  const key = Buffer.from(process.env.AES_KEY!, 'hex');
  const iv = Buffer.from(process.env.AES_IV!, 'hex');

  const decipher = crypto.createDecipheriv('aes-256-cbc', key, iv);
  const decrypted = Buffer.concat([decipher.update(buffer), decipher.final()]);
  return decrypted.toString('utf-8');
}
