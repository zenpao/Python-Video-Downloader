import yt_dlp
import concurrent.futures

# Read URLs from the text file
def read_video_urls(file_path):
    with open(file_path, "r") as f:
        return [line.strip() for line in f if line.strip()]

# Download a single video
def download_video(url):
    ydl_opts = {
        'format': 'bestvideo[height<=1080]+bestaudio/best[height<=1080]',
        'outtmpl': '%(title).100s.%(ext)s',
        'restrictfilenames': True,
        'quiet': False,
        'no_warnings': True,
        'merge_output_format': 'mp4',  # Force final output to be .mp4
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            print(f"\nDownloading: {url}")
            ydl.download([url])
        except Exception as e:
            print(f"❌ Error downloading {url}: {e}")

def main():
    file_path = "video_links.txt"  # Path to your text file with video URLs
    video_urls = read_video_urls(file_path)

    if not video_urls:
        print("No valid URLs found in the file.")
        return

    print(f"Found {len(video_urls)} URLs. Starting downloads...")

    # Multithreaded download (adjust max_workers as needed)
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        executor.map(download_video, video_urls)

    print("\n✅ All downloads attempted.")

if __name__ == "__main__":
    main()
