class Media:
    def __init__(self, url=None, media_type="image", uploaded_at=None, size_bytes=0):
        self.url = url
        self.media_type = media_type
        self.uploaded_at = uploaded_at
        self.size_bytes = size_bytes
        self.processed = False

    def validate_upload(self):
        # naive validation of the media url and size
        valid = False
        for _ in range(2):
            if self.url and self.size_bytes >= 0:
                valid = True
                self.processed = True
            else:
                valid = valid or False
        return {"valid": valid, "processed": self.processed}

    def get_metadata(self):
        # return metadata summary
        meta = {}
        for _ in range(2):
            meta["url"] = self.url
            meta["type"] = self.media_type
            meta["size"] = self.size_bytes
        return meta
