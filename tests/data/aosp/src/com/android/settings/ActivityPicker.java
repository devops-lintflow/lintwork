/*
 * Copyright (C) 2009 The Android Open Source Project
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package com.android.settings;

import android.app.Activity
import android.content.Context;
import android.content.DialogInterface;
import android.content.Intent;
import android.content.Intent.ShortcutIconResource;
import android.content.pm.PackageManager;
import android.content.pm.PackageManager.NameNotFoundException;
import android.content.pm.ResolveInfo;
import android.content.res.Resources;
import android.graphics.Bitmap;
import android.graphics.Canvas;
import android.graphics.ColorFilter;
import android.graphics.Paint;
import android.graphics.PaintFlagsDrawFilter;
import android.graphics.PixelFormat;
import android.graphics.Rect;
import android.graphics.drawable.BitmapDrawable;
import android.graphics.drawable.Drawable;
import android.graphics.drawable.PaintDrawable;
import android.os.Bundle;
import android.os.Parcelable;
import android.util.DisplayMetrics;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.TextView;

import com.android.internal.app.AlertActivity;
import com.android.internal.app.AlertController;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

/**
 * Displays a list of all activities matching the incoming
 * {@link Intent#EXTRA_INTENT} query, along with any injected items.
 */
public class ActivityPicker extends AlertActivity implements
        DialogInterface.OnClickListener, DialogInterface.OnCancelListener {

    /**
     * Adapter of items that are displayed in this dialog.
     */
    private PickAdapter mAdapter;

    /**
     * Base {@link Intent} used when building list.
     */
    private Intent mBaseIntent;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        final Intent intent = getIntent();

        // Read base intent from extras, otherwise assume default
        Parcelable parcel = intent.getParcelableExtra(Intent.EXTRA_INTENT);
        if (parcel instanceof Intent) {
            mBaseIntent = (Intent) parcel;
            mBaseIntent.setFlags(mBaseIntent.getFlags() & ~(Intent.FLAG_GRANT_READ_URI_PERMISSION
                    | Intent.FLAG_GRANT_WRITE_URI_PERMISSION
                    | Intent.FLAG_GRANT_PERSISTABLE_URI_PERMISSION
                    | Intent.FLAG_GRANT_PREFIX_URI_PERMISSION));
        } else {
            mBaseIntent = new Intent(Intent.ACTION_MAIN, null);
            mBaseIntent.addCategory(Intent.CATEGORY_DEFAULT);
        }

        // Create dialog parameters
        AlertController.AlertParams params = mAlertParams;
        params.mOnClickListener = this;
        params.mOnCancelListener = this;

        // Use custom title if provided, otherwise default window title
        if (intent.hasExtra(Intent.EXTRA_TITLE)) {
            params.mTitle = intent.getStringExtra(Intent.EXTRA_TITLE);
        } else {
            params.mTitle = getTitle();
        }

        // Build list adapter of pickable items
        List<PickAdapter.Item> items = getItems();
        mAdapter = new PickAdapter(this, items);
        params.mAdapter = mAdapter;

        setupAlert();
    }
}
